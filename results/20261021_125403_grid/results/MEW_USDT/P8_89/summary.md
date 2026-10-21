# EMA Hourly Continuation — MEW/USDT P8_89

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7799 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -1.6162 |
| sortino_ratio | -0.5202 |
| max_drawdown | 0.4901 |
| cagr | -0.2139 |
| net_avg_win | 64.8199 |
| net_avg_loss | -78.9713 |
| avg_hold_time_bars | 26.2299 |
| exposure | 0.6069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
