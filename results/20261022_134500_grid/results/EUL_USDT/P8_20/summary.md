# EMA Hourly Continuation — EUL/USDT P8_20

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1506 |
| net_profit_factor | 0.3237 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.6260 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -11.9341 |
| sortino_ratio | -6.5456 |
| max_drawdown | 0.9997 |
| cagr | -0.9622 |
| net_avg_win | 7.9735 |
| net_avg_loss | -16.3151 |
| avg_hold_time_bars | 3.9495 |
| exposure | 0.2704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
