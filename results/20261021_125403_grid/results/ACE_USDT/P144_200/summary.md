# EMA Hourly Continuation — ACE/USDT P144_200

**Symbol:** ACE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.5198 |
| gross_profit_factor | 1.0784 |
| gross_win_rate | 0.5198 |
| sharpe_ratio | -0.9835 |
| sortino_ratio | -0.2130 |
| max_drawdown | 0.3217 |
| cagr | -0.0934 |
| net_avg_win | 78.2466 |
| net_avg_loss | -104.8204 |
| avg_hold_time_bars | 8.5991 |
| exposure | 0.0883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
