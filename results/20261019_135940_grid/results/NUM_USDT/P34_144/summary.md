# EMA Hourly Continuation — NUM/USDT P34_144

**Symbol:** NUM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.5388 |
| net_win_rate | 0.4054 |
| gross_profit_factor | 0.7520 |
| gross_win_rate | 0.4093 |
| sharpe_ratio | -4.8194 |
| sortino_ratio | -1.5377 |
| max_drawdown | 0.8528 |
| cagr | -0.5196 |
| net_avg_win | 46.7966 |
| net_avg_loss | -59.2227 |
| avg_hold_time_bars | 17.4691 |
| exposure | 0.4113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
