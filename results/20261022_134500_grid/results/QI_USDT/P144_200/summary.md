# EMA Hourly Continuation — QI/USDT P144_200

**Symbol:** QI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.4393 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -4.7467 |
| sortino_ratio | -1.3586 |
| max_drawdown | 0.8179 |
| cagr | -0.4893 |
| net_avg_win | 33.4829 |
| net_avg_loss | -63.8557 |
| avg_hold_time_bars | 5.2697 |
| exposure | 0.0999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
