# EMA Hourly Continuation — TNSR/USDT P55_89

**Symbol:** TNSR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.0079 |
| sortino_ratio | -1.8268 |
| max_drawdown | 0.8951 |
| cagr | -0.5870 |
| net_avg_win | 40.4233 |
| net_avg_loss | -61.0652 |
| avg_hold_time_bars | 4.4354 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
