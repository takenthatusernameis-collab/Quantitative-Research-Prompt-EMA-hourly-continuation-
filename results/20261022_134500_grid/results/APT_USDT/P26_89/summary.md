# EMA Hourly Continuation — APT/USDT P26_89

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5472 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -5.4171 |
| sortino_ratio | -2.0818 |
| max_drawdown | 0.9260 |
| cagr | -0.6351 |
| net_avg_win | 33.0125 |
| net_avg_loss | -49.5850 |
| avg_hold_time_bars | 9.0120 |
| exposure | 0.3060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
