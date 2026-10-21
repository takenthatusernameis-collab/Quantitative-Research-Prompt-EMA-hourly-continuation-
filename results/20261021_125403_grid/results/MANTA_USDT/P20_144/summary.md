# EMA Hourly Continuation — MANTA/USDT P20_144

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.1832 |
| sortino_ratio | -0.3093 |
| max_drawdown | 0.3069 |
| cagr | -0.1338 |
| net_avg_win | 80.9798 |
| net_avg_loss | -95.3691 |
| avg_hold_time_bars | 39.3373 |
| exposure | 0.5990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
