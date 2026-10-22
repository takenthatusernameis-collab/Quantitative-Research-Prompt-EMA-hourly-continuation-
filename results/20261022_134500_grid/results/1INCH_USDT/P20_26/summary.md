# EMA Hourly Continuation — 1INCH/USDT P20_26

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1326 |
| net_profit_factor | 0.1822 |
| net_win_rate | 0.3477 |
| gross_profit_factor | 0.6593 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -15.9122 |
| sortino_ratio | -8.5103 |
| max_drawdown | 1.0000 |
| cagr | -0.9890 |
| net_avg_win | 4.8313 |
| net_avg_loss | -14.1354 |
| avg_hold_time_bars | 1.8967 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
