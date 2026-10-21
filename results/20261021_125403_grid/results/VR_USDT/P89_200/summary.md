# EMA Hourly Continuation — VR/USDT P89_200

**Symbol:** VR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.4909 |
| net_win_rate | 0.3648 |
| gross_profit_factor | 0.5891 |
| gross_win_rate | 0.3648 |
| sharpe_ratio | -3.5836 |
| sortino_ratio | -0.7847 |
| max_drawdown | 0.6011 |
| cagr | -0.3065 |
| net_avg_win | 65.1316 |
| net_avg_loss | -76.1782 |
| avg_hold_time_bars | 16.0041 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
