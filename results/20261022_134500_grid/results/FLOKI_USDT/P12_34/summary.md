# EMA Hourly Continuation — FLOKI/USDT P12_34

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1352 |
| net_profit_factor | 0.4737 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7557 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -10.4680 |
| sortino_ratio | -5.4182 |
| max_drawdown | 0.9989 |
| cagr | -0.9335 |
| net_avg_win | 16.1122 |
| net_avg_loss | -23.9038 |
| avg_hold_time_bars | 4.0207 |
| exposure | 0.2471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
