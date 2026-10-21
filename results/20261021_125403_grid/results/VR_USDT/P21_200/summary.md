# EMA Hourly Continuation — VR/USDT P21_200

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.7154 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8578 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -1.8232 |
| sortino_ratio | -0.4239 |
| max_drawdown | 0.4027 |
| cagr | -0.1795 |
| net_avg_win | 79.3785 |
| net_avg_loss | -94.2322 |
| avg_hold_time_bars | 50.1778 |
| exposure | 0.6158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
