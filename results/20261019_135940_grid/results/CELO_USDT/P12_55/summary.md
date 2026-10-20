# EMA Hourly Continuation — CELO/USDT P12_55

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9720 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -5.1426 |
| sortino_ratio | -2.2567 |
| max_drawdown | 0.9345 |
| cagr | -0.6561 |
| net_avg_win | 31.9937 |
| net_avg_loss | -47.1378 |
| avg_hold_time_bars | 9.3691 |
| exposure | 0.4112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
