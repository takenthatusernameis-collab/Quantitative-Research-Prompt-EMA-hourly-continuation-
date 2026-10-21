# EMA Hourly Continuation — APT/USDT P8_100

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.9510 |
| net_win_rate | 0.5328 |
| gross_profit_factor | 1.1257 |
| gross_win_rate | 0.5328 |
| sharpe_ratio | -0.2536 |
| sortino_ratio | -0.0728 |
| max_drawdown | 0.2012 |
| cagr | -0.0389 |
| net_avg_win | 87.1958 |
| net_avg_loss | -104.5764 |
| avg_hold_time_bars | 39.0808 |
| exposure | 0.7035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
