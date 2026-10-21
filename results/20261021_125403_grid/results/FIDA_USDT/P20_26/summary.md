# EMA Hourly Continuation — FIDA/USDT P20_26

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5949 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9109 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.9304 |
| sortino_ratio | -0.7886 |
| max_drawdown | 0.6000 |
| cagr | -0.3030 |
| net_avg_win | 51.9354 |
| net_avg_loss | -80.1885 |
| avg_hold_time_bars | 4.9915 |
| exposure | 0.0797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
