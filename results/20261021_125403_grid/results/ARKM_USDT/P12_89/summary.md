# EMA Hourly Continuation — ARKM/USDT P12_89

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.7851 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.8029 |
| sortino_ratio | -0.5763 |
| max_drawdown | 0.5335 |
| cagr | -0.2338 |
| net_avg_win | 73.3137 |
| net_avg_loss | -86.9437 |
| avg_hold_time_bars | 22.6448 |
| exposure | 0.5188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
