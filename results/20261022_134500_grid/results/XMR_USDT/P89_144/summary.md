# EMA Hourly Continuation — XMR/USDT P89_144

**Symbol:** XMR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.3034 |
| net_win_rate | 0.3990 |
| gross_profit_factor | 0.7487 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -9.3974 |
| sortino_ratio | -3.8016 |
| max_drawdown | 0.9921 |
| cagr | -0.8542 |
| net_avg_win | 13.5022 |
| net_avg_loss | -29.5462 |
| avg_hold_time_bars | 3.1259 |
| exposure | 0.1140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
