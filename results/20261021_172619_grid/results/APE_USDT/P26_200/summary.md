# EMA Hourly Continuation — APE/USDT P26_200

**Symbol:** APE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.7135 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8479 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -1.5825 |
| sortino_ratio | -0.3625 |
| max_drawdown | 0.3610 |
| cagr | -0.1544 |
| net_avg_win | 70.7331 |
| net_avg_loss | -86.2981 |
| avg_hold_time_bars | 49.9423 |
| exposure | 0.5902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
