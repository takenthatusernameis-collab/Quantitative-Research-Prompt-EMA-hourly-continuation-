# EMA Hourly Continuation — ONE/USDT P8_12

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.8388 |
| net_win_rate | 0.5286 |
| gross_profit_factor | 1.1312 |
| gross_win_rate | 0.5330 |
| sharpe_ratio | -0.8222 |
| sortino_ratio | -0.1789 |
| max_drawdown | 0.2456 |
| cagr | -0.0795 |
| net_avg_win | 81.3943 |
| net_avg_loss | -108.8301 |
| avg_hold_time_bars | 4.1718 |
| exposure | 0.0430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
