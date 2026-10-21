# EMA Hourly Continuation — APT/USDT P26_144

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.9557 |
| net_win_rate | 0.5403 |
| gross_profit_factor | 1.1583 |
| gross_win_rate | 0.5403 |
| sharpe_ratio | -0.1955 |
| sortino_ratio | -0.0517 |
| max_drawdown | 0.1689 |
| cagr | -0.0288 |
| net_avg_win | 84.3611 |
| net_avg_loss | -103.7476 |
| avg_hold_time_bars | 32.4776 |
| exposure | 0.4945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
