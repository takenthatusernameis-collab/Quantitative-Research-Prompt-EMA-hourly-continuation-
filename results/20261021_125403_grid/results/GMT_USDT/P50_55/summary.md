# EMA Hourly Continuation — GMT/USDT P50_55

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.2431 |
| sortino_ratio | -0.1872 |
| max_drawdown | 0.2076 |
| cagr | -0.0822 |
| net_avg_win | 79.2160 |
| net_avg_loss | -110.9794 |
| avg_hold_time_bars | 4.9455 |
| exposure | 0.0247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
