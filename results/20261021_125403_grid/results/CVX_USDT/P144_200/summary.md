# EMA Hourly Continuation — CVX/USDT P144_200

**Symbol:** CVX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.7942 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0502 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -0.9782 |
| sortino_ratio | -0.2055 |
| max_drawdown | 0.2540 |
| cagr | -0.0905 |
| net_avg_win | 74.3431 |
| net_avg_loss | -99.9692 |
| avg_hold_time_bars | 6.8498 |
| exposure | 0.0663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
