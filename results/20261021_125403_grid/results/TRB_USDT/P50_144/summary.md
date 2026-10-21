# EMA Hourly Continuation — TRB/USDT P50_144

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8118 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -2.7659 |
| sortino_ratio | -0.7401 |
| max_drawdown | 0.6071 |
| cagr | -0.2880 |
| net_avg_win | 64.0038 |
| net_avg_loss | -80.4656 |
| avg_hold_time_bars | 17.0280 |
| exposure | 0.2751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
