# EMA Hourly Continuation — ENJ/USDT P20_144

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.9028 |
| net_win_rate | 0.5232 |
| gross_profit_factor | 1.1001 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -0.6123 |
| sortino_ratio | -0.1684 |
| max_drawdown | 0.3269 |
| cagr | -0.0780 |
| net_avg_win | 89.5876 |
| net_avg_loss | -108.8784 |
| avg_hold_time_bars | 33.8065 |
| exposure | 0.5614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
