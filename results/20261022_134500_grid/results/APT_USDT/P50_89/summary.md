# EMA Hourly Continuation — APT/USDT P50_89

**Symbol:** APT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5349 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9730 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -5.3725 |
| sortino_ratio | -1.9999 |
| max_drawdown | 0.9160 |
| cagr | -0.6230 |
| net_avg_win | 32.2388 |
| net_avg_loss | -53.3873 |
| avg_hold_time_bars | 4.2262 |
| exposure | 0.1333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
