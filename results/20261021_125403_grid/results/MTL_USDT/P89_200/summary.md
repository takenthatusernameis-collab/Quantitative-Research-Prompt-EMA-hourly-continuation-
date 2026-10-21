# EMA Hourly Continuation — MTL/USDT P89_200

**Symbol:** MTL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6240 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8592 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.3627 |
| sortino_ratio | -0.5637 |
| max_drawdown | 0.4849 |
| cagr | -0.2284 |
| net_avg_win | 60.3348 |
| net_avg_loss | -85.0943 |
| avg_hold_time_bars | 17.8475 |
| exposure | 0.2278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
