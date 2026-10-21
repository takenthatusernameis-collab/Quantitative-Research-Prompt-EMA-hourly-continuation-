# EMA Hourly Continuation — ACE/USDT P8_200

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.8434 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9877 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8097 |
| sortino_ratio | -0.1778 |
| max_drawdown | 0.2637 |
| cagr | -0.0800 |
| net_avg_win | 85.8680 |
| net_avg_loss | -101.8116 |
| avg_hold_time_bars | 74.9202 |
| exposure | 0.8069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
