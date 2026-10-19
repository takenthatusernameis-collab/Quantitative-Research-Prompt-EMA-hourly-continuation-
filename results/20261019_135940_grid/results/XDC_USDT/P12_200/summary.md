# EMA Hourly Continuation — XDC/USDT P12_200

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.4085 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -5.8593 |
| sortino_ratio | -2.0175 |
| max_drawdown | 0.9270 |
| cagr | -0.6443 |
| net_avg_win | 23.4942 |
| net_avg_loss | -45.4777 |
| avg_hold_time_bars | 22.3214 |
| exposure | 0.6250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
