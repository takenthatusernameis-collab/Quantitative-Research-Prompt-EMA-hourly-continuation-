# EMA Hourly Continuation — CKB/USDT P20_144

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -4.1336 |
| sortino_ratio | -1.3506 |
| max_drawdown | 0.8117 |
| cagr | -0.4821 |
| net_avg_win | 46.5242 |
| net_avg_loss | -65.4710 |
| avg_hold_time_bars | 21.0623 |
| exposure | 0.5227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
