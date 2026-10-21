# EMA Hourly Continuation — STX/USDT P12_144

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8202 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9720 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.0489 |
| sortino_ratio | -0.2744 |
| max_drawdown | 0.3636 |
| cagr | -0.1203 |
| net_avg_win | 75.0232 |
| net_avg_loss | -90.9247 |
| avg_hold_time_bars | 46.5252 |
| exposure | 0.7095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
