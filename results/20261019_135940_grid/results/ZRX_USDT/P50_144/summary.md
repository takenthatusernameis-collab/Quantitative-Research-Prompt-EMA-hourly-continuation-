# EMA Hourly Continuation — ZRX/USDT P50_144

**Symbol:** ZRX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6064 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -3.4671 |
| sortino_ratio | -1.1254 |
| max_drawdown | 0.7433 |
| cagr | -0.4144 |
| net_avg_win | 44.6564 |
| net_avg_loss | -68.5347 |
| avg_hold_time_bars | 11.3743 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
