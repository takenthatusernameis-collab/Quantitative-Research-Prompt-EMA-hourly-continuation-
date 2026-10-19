# EMA Hourly Continuation — APE/USDT P50_200

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6950 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0021 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -2.0668 |
| sortino_ratio | -0.6016 |
| max_drawdown | 0.5110 |
| cagr | -0.2470 |
| net_avg_win | 54.4990 |
| net_avg_loss | -79.5401 |
| avg_hold_time_bars | 21.1489 |
| exposure | 0.4066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
