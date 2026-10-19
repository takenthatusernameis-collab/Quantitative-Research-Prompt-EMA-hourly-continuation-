# EMA Hourly Continuation — TRX/USDT P89_144

**Symbol:** TRX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.1939 |
| net_win_rate | 0.3608 |
| gross_profit_factor | 0.8287 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -9.1816 |
| sortino_ratio | -2.8267 |
| max_drawdown | 0.9797 |
| cagr | -0.7862 |
| net_avg_win | 15.3949 |
| net_avg_loss | -44.8259 |
| avg_hold_time_bars | 5.3019 |
| exposure | 0.1022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
