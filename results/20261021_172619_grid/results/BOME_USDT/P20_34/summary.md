# EMA Hourly Continuation — BOME/USDT P20_34

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.6130 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.7930 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -2.6724 |
| sortino_ratio | -0.6797 |
| max_drawdown | 0.5783 |
| cagr | -0.2684 |
| net_avg_win | 60.2416 |
| net_avg_loss | -79.3895 |
| avg_hold_time_bars | 5.0906 |
| exposure | 0.0740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
