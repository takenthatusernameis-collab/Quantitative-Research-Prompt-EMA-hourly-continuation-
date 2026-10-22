# EMA Hourly Continuation — EGLD/USDT P12_89

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6543 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -3.5976 |
| sortino_ratio | -1.3036 |
| max_drawdown | 0.8153 |
| cagr | -0.4706 |
| net_avg_win | 45.6020 |
| net_avg_loss | -67.8525 |
| avg_hold_time_bars | 18.5887 |
| exposure | 0.5670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
