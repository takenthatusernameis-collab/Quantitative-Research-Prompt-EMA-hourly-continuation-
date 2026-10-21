# EMA Hourly Continuation — KAS/USDT P34_55

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7305 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.4232 |
| sortino_ratio | -0.3090 |
| max_drawdown | 0.3159 |
| cagr | -0.1313 |
| net_avg_win | 70.1896 |
| net_avg_loss | -97.7787 |
| avg_hold_time_bars | 6.0175 |
| exposure | 0.0624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
