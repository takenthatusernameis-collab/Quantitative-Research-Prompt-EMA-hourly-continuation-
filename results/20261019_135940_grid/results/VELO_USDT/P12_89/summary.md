# EMA Hourly Continuation — VELO/USDT P12_89

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.7323 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -2.9460 |
| sortino_ratio | -1.2160 |
| max_drawdown | 0.7854 |
| cagr | -0.4376 |
| net_avg_win | 49.0860 |
| net_avg_loss | -67.0292 |
| avg_hold_time_bars | 12.3239 |
| exposure | 0.4773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
