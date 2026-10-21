# EMA Hourly Continuation — EDU/USDT P34_200

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7829 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9257 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.3858 |
| sortino_ratio | -0.3610 |
| max_drawdown | 0.3905 |
| cagr | -0.1544 |
| net_avg_win | 76.7718 |
| net_avg_loss | -91.2975 |
| avg_hold_time_bars | 34.0952 |
| exposure | 0.5184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
