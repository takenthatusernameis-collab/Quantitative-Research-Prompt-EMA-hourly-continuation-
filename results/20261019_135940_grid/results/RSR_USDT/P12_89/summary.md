# EMA Hourly Continuation — RSR/USDT P12_89

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.6520 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9378 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -3.9763 |
| sortino_ratio | -1.5544 |
| max_drawdown | 0.8570 |
| cagr | -0.5242 |
| net_avg_win | 43.2603 |
| net_avg_loss | -59.3765 |
| avg_hold_time_bars | 14.3239 |
| exposure | 0.5046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
