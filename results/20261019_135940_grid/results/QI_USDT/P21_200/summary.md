# EMA Hourly Continuation — QI/USDT P21_200

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6661 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.6188 |
| sortino_ratio | -0.7488 |
| max_drawdown | 0.6151 |
| cagr | -0.2994 |
| net_avg_win | 59.4029 |
| net_avg_loss | -82.9259 |
| avg_hold_time_bars | 31.4673 |
| exposure | 0.5881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
