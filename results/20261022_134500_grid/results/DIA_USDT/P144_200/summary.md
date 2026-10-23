# EMA Hourly Continuation — DIA/USDT P144_200

**Symbol:** DIA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.5750 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0314 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -3.3500 |
| sortino_ratio | -0.9322 |
| max_drawdown | 0.7012 |
| cagr | -0.3676 |
| net_avg_win | 47.2919 |
| net_avg_loss | -81.4196 |
| avg_hold_time_bars | 4.5127 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
