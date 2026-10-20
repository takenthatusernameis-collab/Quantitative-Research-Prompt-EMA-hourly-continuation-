# EMA Hourly Continuation — ONT/USDT P20_100

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -3.8679 |
| sortino_ratio | -1.3760 |
| max_drawdown | 0.8117 |
| cagr | -0.4772 |
| net_avg_win | 45.2825 |
| net_avg_loss | -63.0543 |
| avg_hold_time_bars | 14.6708 |
| exposure | 0.4235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
