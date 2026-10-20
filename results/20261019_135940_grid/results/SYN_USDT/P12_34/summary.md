# EMA Hourly Continuation — SYN/USDT P12_34

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1225 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.8166 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -7.8413 |
| sortino_ratio | -3.8487 |
| max_drawdown | 0.9913 |
| cagr | -0.8484 |
| net_avg_win | 17.5095 |
| net_avg_loss | -28.2071 |
| avg_hold_time_bars | 4.6531 |
| exposure | 0.2591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
