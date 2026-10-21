# EMA Hourly Continuation — APT/USDT P34_50

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.8327 |
| net_win_rate | 0.5374 |
| gross_profit_factor | 1.1550 |
| gross_win_rate | 0.5374 |
| sharpe_ratio | -0.8049 |
| sortino_ratio | -0.1705 |
| max_drawdown | 0.2015 |
| cagr | -0.0757 |
| net_avg_win | 77.6193 |
| net_avg_loss | -108.2766 |
| avg_hold_time_bars | 5.3364 |
| exposure | 0.0519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
