# EMA Hourly Continuation — CHR/USDT P89_200

**Symbol:** CHR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6584 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.7901 |
| sortino_ratio | -0.8145 |
| max_drawdown | 0.6201 |
| cagr | -0.3160 |
| net_avg_win | 58.8098 |
| net_avg_loss | -81.6442 |
| avg_hold_time_bars | 11.5532 |
| exposure | 0.2211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
