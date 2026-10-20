# EMA Hourly Continuation — DBR/USDT P8_144

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.5416 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -4.2814 |
| sortino_ratio | -1.3796 |
| max_drawdown | 0.7534 |
| cagr | -0.4917 |
| net_avg_win | 45.7136 |
| net_avg_loss | -68.9606 |
| avg_hold_time_bars | 28.4567 |
| exposure | 0.6910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
