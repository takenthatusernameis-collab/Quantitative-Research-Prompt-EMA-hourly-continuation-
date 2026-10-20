# EMA Hourly Continuation — ALT/USDT P50_100

**Symbol:** ALT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.5867 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9197 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -3.7932 |
| sortino_ratio | -1.2927 |
| max_drawdown | 0.7872 |
| cagr | -0.4541 |
| net_avg_win | 40.1862 |
| net_avg_loss | -62.5966 |
| avg_hold_time_bars | 7.3997 |
| exposure | 0.1944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
