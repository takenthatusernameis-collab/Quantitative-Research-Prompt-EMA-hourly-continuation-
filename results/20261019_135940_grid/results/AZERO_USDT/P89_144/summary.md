# EMA Hourly Continuation — AZERO/USDT P89_144

**Symbol:** AZERO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6129 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9566 |
| sortino_ratio | -0.8620 |
| max_drawdown | 0.6649 |
| cagr | -0.3364 |
| net_avg_win | 48.6031 |
| net_avg_loss | -77.0930 |
| avg_hold_time_bars | 6.8638 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
