# EMA Hourly Continuation — SSV/USDT P89_144

**Symbol:** SSV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.4894 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.8126 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -5.5597 |
| sortino_ratio | -1.8654 |
| max_drawdown | 0.8994 |
| cagr | -0.5919 |
| net_avg_win | 35.1870 |
| net_avg_loss | -55.1659 |
| avg_hold_time_bars | 4.6174 |
| exposure | 0.1174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
