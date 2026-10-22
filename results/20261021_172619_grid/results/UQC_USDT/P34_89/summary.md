# EMA Hourly Continuation — UQC/USDT P34_89

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.2905 |
| net_win_rate | 0.2527 |
| gross_profit_factor | 0.4561 |
| gross_win_rate | 0.2776 |
| sharpe_ratio | -7.4285 |
| sortino_ratio | -1.7617 |
| max_drawdown | 0.9106 |
| cagr | -0.6160 |
| net_avg_win | 52.5132 |
| net_avg_loss | -61.1147 |
| avg_hold_time_bars | 30.4520 |
| exposure | 0.3873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
