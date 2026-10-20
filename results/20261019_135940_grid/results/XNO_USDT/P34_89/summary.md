# EMA Hourly Continuation — XNO/USDT P34_89

**Symbol:** XNO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.4896 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.7964 |
| gross_win_rate | 0.4028 |
| sharpe_ratio | -8.0738 |
| sortino_ratio | -3.3407 |
| max_drawdown | 0.9829 |
| cagr | -0.8009 |
| net_avg_win | 27.6449 |
| net_avg_loss | -37.5306 |
| avg_hold_time_bars | 5.8806 |
| exposure | 0.2283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
