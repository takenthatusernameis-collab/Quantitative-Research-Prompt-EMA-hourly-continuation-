# EMA Hourly Continuation — KNC/USDT P20_34

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.3475 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -10.6638 |
| sortino_ratio | -4.9174 |
| max_drawdown | 0.9981 |
| cagr | -0.9167 |
| net_avg_win | 12.5354 |
| net_avg_loss | -24.8304 |
| avg_hold_time_bars | 4.0144 |
| exposure | 0.1898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
