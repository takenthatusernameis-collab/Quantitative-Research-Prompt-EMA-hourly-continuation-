# EMA Hourly Continuation — MOCA/USDT P8_89

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.6107 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9118 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.8534 |
| sortino_ratio | -1.3661 |
| max_drawdown | 0.7840 |
| cagr | -0.4784 |
| net_avg_win | 44.9033 |
| net_avg_loss | -65.5179 |
| avg_hold_time_bars | 23.3124 |
| exposure | 0.6696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
