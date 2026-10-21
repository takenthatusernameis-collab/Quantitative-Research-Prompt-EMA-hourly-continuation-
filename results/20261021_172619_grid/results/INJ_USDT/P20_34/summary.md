# EMA Hourly Continuation — INJ/USDT P20_34

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8031 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0629 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -1.1273 |
| sortino_ratio | -0.2712 |
| max_drawdown | 0.2821 |
| cagr | -0.1173 |
| net_avg_win | 76.2010 |
| net_avg_loss | -101.2033 |
| avg_hold_time_bars | 5.2115 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
