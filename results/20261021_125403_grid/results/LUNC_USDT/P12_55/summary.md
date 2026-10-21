# EMA Hourly Continuation — LUNC/USDT P12_55

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6164 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.8125 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -4.3111 |
| sortino_ratio | -1.5093 |
| max_drawdown | 0.8327 |
| cagr | -0.5009 |
| net_avg_win | 50.6151 |
| net_avg_loss | -62.0038 |
| avg_hold_time_bars | 11.2463 |
| exposure | 0.3113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
